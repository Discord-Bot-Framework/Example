from __future__ import annotations

import time

import arc

plugin = arc.GatewayPlugin("example")

demo_group = plugin.include_slash_group("demo", "Example commands")
demo_test_group = demo_group.include_subgroup("test", "Example test commands")


@demo_group.include
@arc.slash_subcommand("hello", "Say hello")
async def hello(ctx: arc.GatewayContext) -> None:
    await ctx.respond("Hello.")


@demo_group.include
@arc.slash_subcommand("ping", "Measure command round-trip latency")
async def ping(ctx: arc.GatewayContext) -> None:
    started = time.perf_counter()
    response = await ctx.respond("Pinging...")
    latency_ms = (time.perf_counter() - started) * 1000
    await response.edit(f"Pong! Round-trip latency: {latency_ms:.2f} ms.")


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
