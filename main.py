#!/usr/bin/env python3
"""
Main entry point for the Advanced Calculator application.
"""

if __name__ == "__main__":
    try:
        from app.calculator_repl import CalculatorREPL
        repl = CalculatorREPL()
        repl.run()
    except KeyboardInterrupt:
        print("\n\nCalculator exited.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
