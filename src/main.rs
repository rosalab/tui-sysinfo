mod components;

use std::io::stdout;
use std::sync::Arc;
use std::thread::sleep;
use anyhow::Result;

use ratatui::prelude::*;
use ratatui::widgets::{Block, Borders, Paragraph};
use crate::components::app::App;
use crate::components::sys_info::render_sys_info;

fn main() -> Result<()> {
    let backend = CrosstermBackend::new(stdout());
    let mut terminal = Terminal::new(backend)?;
    let app = App::new();
    terminal.clear();
    loop {
        let _ = terminal.draw(|frame| {
            let layout = Layout::default()
                .direction(Direction::Vertical)
                .constraints(
                    [
                        Constraint::Percentage(10),
                        Constraint::Percentage(90),
                    ]
                        .as_ref(),
                )
                .split(frame.size());
            render_sys_info(Arc::clone(&app.system), frame, layout[0]);
            frame.render_widget(
                Paragraph::new("Bottom")
                    .block(Block::new().borders(Borders::ALL)),
                layout[1]
            );
        });
        sleep(std::time::Duration::from_secs(1));
    }
}
