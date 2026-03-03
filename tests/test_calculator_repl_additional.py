"""Additional tests for CalculatorREPL branches and command handling."""
import pytest
from app.calculator_repl import CalculatorREPL


def test_show_help_outputs_operations_and_help(capsys):
    repl = CalculatorREPL()
    repl.show_help()
    captured = capsys.readouterr()
    assert "Available commands" in captured.out
    assert "Operations:" in captured.out


def test_show_history_empty(capsys):
    repl = CalculatorREPL()
    repl.show_history()
    captured = capsys.readouterr()
    assert "No history" in captured.out


def test_clear_prints_message(capsys):
    repl = CalculatorREPL()
    repl.process_command('clear')
    captured = capsys.readouterr()
    assert "History cleared" in captured.out


def test_undo_redo_nothing(capsys):
    repl = CalculatorREPL()
    repl.process_command('undo')
    repl.process_command('redo')
    captured = capsys.readouterr()
    assert "Nothing to undo" in captured.out
    assert "Nothing to redo" in captured.out


def test_save_load_usage_messages(capsys):
    repl = CalculatorREPL()
    repl.process_command('save')
    repl.process_command('load')
    captured = capsys.readouterr()
    assert "Usage: save <filename>" in captured.out
    assert "Usage: load <filename>" in captured.out


def test_exit_raises_keyboardinterrupt():
    repl = CalculatorREPL()
    with pytest.raises(KeyboardInterrupt):
        repl.process_command('exit')


def test_unknown_command_prints_help_message(capsys):
    repl = CalculatorREPL()
    repl.process_command('nonexistentcmd')
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out


def test_operation_usage_and_result(capsys):
    repl = CalculatorREPL()
    # missing argument -> usage message
    repl.process_command('add 1')
    captured = capsys.readouterr()
    assert "Usage: add <a> <b>" in captured.out

    # valid operation -> should print result
    repl.process_command('add 2 3')
    captured = capsys.readouterr()
    assert "Result:" in captured.out
