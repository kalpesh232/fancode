import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import filter_fancode_users, calculate_task_completion_percentage

def test_filter_fancode_users():
    users = [
        {"id": 1, "address": {"geo": {"lat": "-35", "lng": "50"}}},
        {"id": 2, "address": {"geo": {"lat": "10", "lng": "90"}}},
    ]
    fancode_users = filter_fancode_users(users)
    assert len(fancode_users) == 1

def test_calculate_task_completion_percentage():
    todos = [
        {"userId": 1, "completed": True},
        {"userId": 1, "completed": False},
        {"userId": 1, "completed": True},
    ]
    percentage = calculate_task_completion_percentage(1, todos)
    assert percentage == 66.66666666666666
