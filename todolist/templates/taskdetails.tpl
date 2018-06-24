<html><body>
<form method='get'>{% csrf_token %}
</form>
<h1>{{ header }}</h1>
<form action="/getlists/{{ list_id }}/gettasks/{{ details.id }}/"method='post'>{% csrf_token %}
<h2>Update task</h2>
<p>Title: <input type="text" value="{{ details.name }}" name="title"></p>
<p>Date created: {{ details.date_created }}</p>
<p>Date modified: {{ details.date_modified }}</p>
<p>Description: <input type="text" value="{{ details.description }}" name="description"></p>
<p>Priority:</p> 
<select name="priority"> 
{% if details.priority == "h" %} <option value="h" selected>High</option> 
{% else %} <option value="h">High</option> 
{% endif %} 
{% if details.priority == "m" %} <option value="m" selected>Medium</option> 
{% else %} <option value="m">Medium</option> 
{% endif %} 
{% if details.priority == "l" %} <option value="l" selected>Low</option> 
{% else %} <option value="l">Low</option> 
{% endif %} 
{% if details.priority == "n" %} <option value="n" selected>None</option> 
{% else %} <option value="n">None</option> 
{% endif %} 
</select>
{% if details.completed %} 
<p>Completed:<input type="checkbox" checked name="completed"></p> 
{% else %} 
<p>Completed: <input type="checkbox" name="completed"></p> 
{% endif %}
<p>Due date: <input type="date" value="{{ details.due_date }}" name="due_date"></p>
<p>Tags: <input type="text" name="tags"></p>
<p>Tags:{{ details.tags }}</p>
<input type="submit" value="update">
</form>
<a href="/getlists/{{ list_id }}/gettasks/">Back to tasks</a><br>
<a href="/getlists/">Back to task lists</a><br>
<a href="delete/">delete task</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>