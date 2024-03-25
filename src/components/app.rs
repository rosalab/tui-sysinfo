use std::sync::{Arc, Mutex};
use sysinfo::System;

pub struct App {
    pub system: Arc<Mutex<System>>,
}

impl App {
    pub fn new() -> App {
        let mut system = System::new_all();
        system.refresh_all();
        App {
            system: Arc::new(Mutex::new(system)),
        }
    }
}