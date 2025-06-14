"""Entry point for the algorithm toolbox application."""

import logging
import sys

from rich.console import Console

from app.utils.interactivity.launcher import AlgorithmLauncher
from app.utils.interactivity.menu import AlgorithmMenu, display_welcome
from app.utils.interactivity.parser import parse_args
from app.utils.logging.logging_config import get_logger, setup_logging

console = Console()


def main() -> None:
    """Main entry point of the application."""
    # Parse command line arguments
    args = parse_args()

    # Setup logging with debug level if requested
    log_level = logging.DEBUG if args.debug else logging.INFO
    setup_logging(level=log_level)

    logger = get_logger(__name__)
    logger.debug("Starting Algorithm Toolbox application")

    if args.debug:
        logger.debug("Debug mode enabled")
        console.print("[dim]🐛 Mode debug activé[/dim]")

    try:
        # Initialize launcher
        launcher = AlgorithmLauncher()
        launcher.load_data()

        display_welcome()

        # Determine mode: interactive menu or direct algorithm execution
        if args.mode is None:
            # Interactive menu mode
            logger.debug("No algorithm specified, starting interactive mode")
            menu = AlgorithmMenu()
            algorithm = menu.run_interactive_mode()

            if algorithm is None:
                logger.debug("User quit interactive mode")
                sys.exit(0)
        else:
            # Direct execution mode
            algorithm = args.mode
            logger.debug(f"Direct execution mode for algorithm: {algorithm}")

        # Execute the selected algorithm
        result, exec_time = launcher.execute_algorithm(algorithm, debug=args.debug)

        # Display results
        launcher.display_results(result, exec_time, algorithm)

        logger.debug("Application completed successfully")

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interruption utilisateur[/yellow]")
        logger.debug("Application interrupted by user")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]❌ Erreur: {e}[/red]")
        logger.error(f"Application error: {e}")
        if args.debug:
            console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
