<h1>{{ header }}</h1>
<ul>
{% if tasks %}
{% for task in tasks %}
	<li><a href="{{ task.id }}/">{{ task.name }}</a></li>
{% endfor %}
{% else %}
<p>There isn't any tasks</p>
{% endif %}
</ul><br>
<a href="/getlists/">Back to task lists</a><br>
<a href="/logout/">LOGOUT</a>
</body></html>