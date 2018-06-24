<html><body>
<form method='get'>{% csrf_token %}
</form>
<h1>{{ header }}</h1>
<form action="/getlists/{{ details.id }}/"method='post'>{% csrf_token %}
<h2>Update your task list</h2>

{% if user == details.owner %} 
<p>Title: <input type="text" value="{{ details.name }}" name="title"></p>
{% if details.tasks %}
<p>Tasks: <a href="gettasks/">{{ details.tasks }}</a></p>
{% else %}
<p>You do not have any tasks</p>
<a href="gettasks/">Create new task</a>
{% endif %}
<p>Friend to share: <input type="text" value="{{ details.friend }}" name="friend"></p>
<p>Owner: {{ details.owner }}</p>
<input type="submit" value="update"><br>
<a href="delete/">delete list</a><br>

{% else %} 
<p>Title: {{ details.name }}</p>
{% if details.tasks %}
<p>Tasks: <a href="sharegettasks/">{{ details.tasks }}</a></p>
{% endif %}
<p>Owner: {{ details.owner }}</p>
{% endif %}
</form>
<a href="/getlists/">Back to task lists</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>