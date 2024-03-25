use std::sync::{Arc, Mutex};
use ratatui::Frame;
use ratatui::layout::{Constraint, Direction, Layout, Rect};
use sysinfo::{System, Disks};
use anyhow::Result;
use ratatui::prelude::*;
use ratatui::style::palette::tailwind;
use ratatui::widgets::{Block, Borders, BorderType, Gauge, LineGauge, Padding, Paragraph};
use ratatui::widgets::block::Title;

const RED: Color = tailwind::RED.c800;
const GREEN: Color = tailwind::GREEN.c800;
const BLUE: Color = tailwind::BLUE.c800;
const ORANGE: Color = tailwind::ORANGE.c800;
const SLATE: Color = tailwind::SLATE.c200;

pub fn render_sys_info(systemState: Arc<Mutex<System>>, frame: &mut Frame, area: Rect) -> Result<()> {
    let mut system = systemState.lock().unwrap();
    system.refresh_cpu();
    system.refresh_memory();
    let global_cpu_counts = system.cpus().len();
    // FIXME: get rid of unwrap, this is can over 100%
    let cpu_usage = system.global_cpu_info().cpu_usage() as f64 / global_cpu_counts as f64;
    let mem_usage = system.used_memory() as f64 / system.total_memory() as f64;
    // get disk usage
    let disks = Disks::new_with_refreshed_list();
    let mut total_disk_space = 0;
    let mut total_disk_available_space = 0;
    for disk in disks.list() {
        total_disk_space += disk.total_space();
        total_disk_available_space += disk.available_space();
    }
    let disk_usage = 1.0 - (total_disk_available_space as f64 / total_disk_space as f64);
    let layout = Layout::default()
        .direction(Direction::Horizontal)
        .constraints(
            [
                Constraint::Percentage(25),
                Constraint::Percentage(5),
                Constraint::Percentage(25),
                Constraint::Percentage(5),
                Constraint::Percentage(25),
            ]
                .as_ref(),
        )
        .split(area);
    render_sys_info_widgets(frame, "CPU", cpu_usage, layout[0]);
    render_sys_info_widgets(frame, "MEM", mem_usage, layout[2]);
    render_sys_info_widgets(frame, "DISK", disk_usage, layout[4]);
    Ok(())
}

fn render_sys_info_widgets(frame: &mut Frame, title: &str, num: f64, area: Rect) {
    let ratio_num = if num >= 1.0 {
        1.0
    } else {
        num
    };
    let color = if num >= 0.8 {
        RED
    } else if num >= 0.6 {
        ORANGE
    } else if num >= 0.4 {
        BLUE
    } else {
        GREEN
    };
    let gauge = LineGauge::default()
        .block(title_block(title))
        .gauge_style(color)
        .line_set(symbols::line::THICK)
        .ratio(ratio_num);
    frame.render_widget(gauge, area);
}

fn title_block(title: &str) -> Block {
    let title = Title::from(title).alignment(Alignment::Center);
    Block::default()
        .title(title)
        .title_style(Style::new().italic())
        .borders(Borders::ALL)
        .border_type(BorderType::Rounded)
        .fg(tailwind::SLATE.c200)
}