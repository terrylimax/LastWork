<html><body>
<h1>{{ header }}</h1>
<ul>
{% if lists %}
{% for list in lists %}
	<li><a href="{{ list.id }}/">{{ list.name }} ({{ list.owner }})</a></li>
{% endfor %}
{% else%}
<p>You do not have any lists</p>
{% endif %}
</ul><br>
<form action="/getlists/"method='post'>{% csrf_token %}
<h2>Create new task list</h2>
<p>Title: <input type="text" name="title"></p><br>
<p>Friend to share: <input type="text" name="friend"></p><br>
<input type="submit" value="create">
</form>
<a href="getusers/">USERS</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>