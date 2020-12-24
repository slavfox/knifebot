// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.
//
// Copyright 2020, Slavfox.
mod commands;

use std::{collections::HashSet, env};

use serenity::{
    async_trait,
    client::{Client, Context, EventHandler},
    framework::standard::{macros::group, StandardFramework},
    http::Http,
    model::{event::ResumedEvent, gateway::Ready, id::UserId},
};

use crate::commands::ping::*;

struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn ready(&self, _: Context, ready: Ready) {
        println!("Connected as {}", ready.user.name);
    }

    async fn resume(&self, _: Context, _: ResumedEvent) {
        println!("Resumed");
    }
}

#[group]
#[commands(ping)]
struct General;

#[tokio::main]
async fn main() {
    let token = env::var("DISCORD_TOKEN")
        .expect("Expected a token in the environment");

    let http = Http::new_with_token(&token);

    let owners: HashSet<UserId> =
        [http.get_current_application_info().await.unwrap().owner.id]
            .iter()
            .cloned()
            .collect();

    let framework = StandardFramework::new()
        .configure(|c| c.owners(owners).prefix("~"))
        .group(&GENERAL_GROUP);

    let mut client = Client::builder(&token)
        .event_handler(Handler)
        .framework(framework)
        .await
        .unwrap();

    if let Err(err) = client.start().await {
        println!("Could not start knifebot: {:?}", err);
    }
}
