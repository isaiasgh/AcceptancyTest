from behave import given, when, then
from todo_list import ToDoList


# Scenario 1: Add a task
@given('the to-do list is empty')
def step_given_empty_list(context):
    context.todo = ToDoList()

@when('the user adds a task "{task_title}"')
def step_when_add_task(context, task_title):
    context.todo.add_task(task_title)

@then('the to-do list should contain "{task_title}"')
def step_then_contains_task(context, task_title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert task_title in titles


# Scenario 2: List all tasks
@given('the to-do list contains tasks')
def step_given_list_with_tasks(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(title=row['Task'])

@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.listed_tasks = context.todo.list_tasks()

@then('the output should contain')
def step_then_output_should_contain(context):
    expected_titles = [row['Task'] for row in context.table]
    actual_titles = [task.title for task in context.listed_tasks]
    for title in expected_titles:
        assert title in actual_titles


# Scenario 3: Mark a task as completed
@given('the to-do list contains tasks with status')
def step_given_tasks_with_status(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(title=row['Task'])
        if row.get('Status') == 'Completed':
            context.todo.mark_task_completed(row['Task'])

@when('the user marks task "{task_title}" as completed')
def step_when_mark_task_completed(context, task_title):
    context.todo.mark_task_completed(task_title)

@then('the to-do list should show task "{task_title}" as completed')
def step_then_task_should_be_completed(context, task_title):
    for task in context.todo.list_tasks():
        if task.title == task_title:
            assert task.completed is True
            return
    assert False, f'Task "{task_title}" not found'


# Scenario 4: Clear the entire to-do list
@when('the user clears the to-do list')
def step_when_clear_todo_list(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    assert len(context.todo.list_tasks()) == 0


# Scenario 5: Remove a task
@when('the user removes the task "{task_title}"')
def step_when_remove_task(context, task_title):
    context.todo.remove_task(task_title)

@then('the to-do list should not contain "{task_title}"')
def step_then_list_should_not_contain(context, task_title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert task_title not in titles


# Scenario 6: Filter completed tasks
@when('the user filters tasks by completed')
def step_when_filter_completed(context):
    context.filtered_tasks = context.todo.list_tasks_by_status(completed=True)

@then('the output should contain only')
def step_then_output_should_contain_only(context):
    expected_titles = [row['Task'] for row in context.table]
    actual_titles = [task.title for task in context.filtered_tasks]
    assert sorted(expected_titles) == sorted(actual_titles)