<html><body>
<form method='get'>{% csrf_token %}
</form>
<h1>{{ header }}</h1>
<p>Title: {{ details.name }}</p>
<p>Date created: {{ details.date_created }}</p>
<p>Date modified: {{ details.date_modified }}</p>
<p>Description: {{ details.description }}</p>
<p>Priority:{{ details.priority }}</p> 
<p>Completed:{{ details.completed }}
<p>Due date:{{ details.due_date }}</p>
<p>Tags:{{ details.tags }}</p>
<a href="/getlists/">Back to task lists</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>