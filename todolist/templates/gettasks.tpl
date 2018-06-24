<html><body>
<form method='get'>{% csrf_token %}
</form>
<h1>{{ header }}</h1>
<ul>
{% if tasks %}
{% for task in tasks %}
	<li><a href="{{ task.id }}/">{{ task.name }}</a></li>
{% endfor %}
{% else %}
<p>You do not have any tasks</p>
{% endif %}
</ul><br>
<form action="/getlists/{{ list_id }}/gettasks/"method='post'>{% csrf_token %}
<h2>Create new task</h2>
<p>Title: <input type="text" name="title"></p>
<p>Description: <input type="text" name="description"></p>
<p>Priority: <select name="priority">
<option value="h">High</option>
<option value="m">Medium</option>
<option value="l">Low</option>
<option value="n">None</option>
</select></p>
<p>Completed: <input type="checkbox" name="completed"></p>
<p>Due date: <input type="date" name="due_date"></p>
<p>Tags: <input type="text" name="tags"></p>
<input type="submit" value="create">
</form>
<a href="/getlists/">Back to task lists</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>