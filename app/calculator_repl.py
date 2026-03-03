"""REPL interface for calculator."""
from app.calculator import Calculator

class CalculatorREPL:
    """Read-Eval-Print Loop for calculator."""
    
    def __init__(self):
        """Initialize REPL."""
        self.calculator = Calculator()
    
    def run(self) -> None:
        """Run REPL."""
        print("Calculator REPL. Type 'help' for commands.")
        
        while True:
            try:
                user_input = input("> ").strip()
                if not user_input:
                    continue
                
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def process_command(self, user_input: str) -> None:
        """Process user command."""
        parts = user_input.split()
        if not parts:
            return
        
        command = parts[0].lower()
        
        if command == 'help':
            self.show_help()
        elif command == 'history':
            self.show_history()
        elif command == 'clear':
            self.calculator.clear_history()
            print("History cleared")
        elif command == 'undo':
            result = self.calculator.undo()
            if result:
                print(f"Undo: {result}")
            else:
                print("Nothing to undo")
        elif command == 'redo':
            result = self.calculator.redo()
            if result:
                print(f"Redo: {result}")
            else:
                print("Nothing to redo")
        elif command == 'save':
            if len(parts) < 2:
                print("Usage: save <filename>")
            else:
                self.calculator.save_history(parts[1])
                print(f"Saved to {parts[1]}")
        elif command == 'load':
            if len(parts) < 2:
                print("Usage: load <filename>")
            else:
                self.calculator.load_history(parts[1])
                print(f"Loaded from {parts[1]}")
        elif command == 'exit':
            raise KeyboardInterrupt()
        elif command in self.calculator.get_available_operations():
            if len(parts) != 3:
                print(f"Usage: {command} <a> <b>")
            else:
                try:
                    result = self.calculator.perform_operation(parts[1], parts[2], command)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
        else:
            print("Unknown command. Type 'help' for commands.")
    
    def show_help(self) -> None:
        """Show help message."""
        print("\nAvailable commands:")
        print("Operations:", ", ".join(self.calculator.get_available_operations()))
        print("history - Show history")
        print("clear - Clear history")
        print("undo - Undo last operation")
        print("redo - Redo last undone")
        print("save <file> - Save history")
        print("load <file> - Load history")
        print("help - Show this help")
        print("exit - Exit calculator\n")
    
    def show_history(self) -> None:
        """Show calculation history."""
        history = self.calculator.get_history()
        if not history:
            print("No history")
            return
        
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
