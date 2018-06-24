<html><body>
<form method='get'>{% csrf_token %}
</form>
<h1>{{ header }}</h1>
<ul>
{% for user in users %}
	<li><h3>{{ header1 }}</h3></li>
        <p>{{ user.first_name }}</p>
	<h3>{{ header2 }}</h3>
        <p>{{ user.last_name }}</p>
	<h3>{{ header3 }}</h3>
        <p>{{ user.email }}</p>
{% endfor %}
</ul><br>
<a href="/logout/">LOGOUT</a>
</body></html>
