import argparse

from dotenv import load_dotenv

load_dotenv()

from src.webui.interface import create_ui, theme_map


def main():
    parser = argparse.ArgumentParser(description="Gradio UI for The Browser")
    parser.add_argument(
        "--ip",
        type=str,
        default="127.0.0.1",
        help="IP address to bind to",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7788,
        help="Port to listen on",
    )
    parser.add_argument(
        "--theme",
        type=str,
        default="Ocean",
        choices=theme_map.keys(),
        help="Theme to use for the Gradio UI",
    )
    args = parser.parse_args()

    demo = create_ui(theme_name=args.theme)
    demo.queue().launch(server_name=args.ip, server_port=args.port)


if __name__ == "__main__":
    main()
