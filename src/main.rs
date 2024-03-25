mod components;

use std::io::stdout;
use std::sync::Arc;
use std::thread::sleep;
use anyhow::Result;
use crossterm::event;
use crossterm::event::{Event, KeyCode};
use crossterm::terminal::{disable_raw_mode, enable_raw_mode};

use ratatui::prelude::*;
use ratatui::widgets::{Block, Borders, Paragraph};
use crate::components::app::App;
use crate::components::sys_info::{render_active_user, render_sys_info};

fn main() -> Result<()> {
    let backend = CrosstermBackend::new(stdout());
    let mut terminal = Terminal::new(backend)?;
    let app = App::new();
    terminal.clear();
    enable_raw_mode()?;
    loop {
        let _ = terminal.draw(|frame| {
            let layout = Layout::default()
                .direction(Direction::Vertical)
                .constraints(
                    [
                        Constraint::Percentage(10),
                        Constraint::Percentage(20),
                        Constraint::Percentage(70),
                    ]
                        .as_ref(),
                )
                .split(frame.size());
            let _ = render_sys_info(Arc::clone(&app.system), frame, layout[0]);
            let _ = render_active_user(frame, layout[1]);
            frame.render_widget(
                Paragraph::new("Bottom")
                    .block(Block::new().borders(Borders::ALL)),
                layout[2]
            );
        });
        sleep(std::time::Duration::from_secs(1));
        if let Event::Key(key) = event::read()? {
            #[allow(clippy::single_match)]
            match key.code {
                KeyCode::Char('q') => {
                    break;
                }
                _ => {}
            };
        }
    }
    disable_raw_mode()?;
    Ok(())
}
