import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from map_gen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (0xd7, 0x99, 0x21))
    entities = {player}
    game_map = game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

    engine = Engine(event_handler=event_handler, player=player, game_map=game_map)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Kitty Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()