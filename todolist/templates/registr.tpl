<html><body>

    <form action="http://127.0.0.1:8080/login/registr/" method='post'>
        {% csrf_token %}
    {{form.as_p}}
    <input type="submit", value = "Registrate"/>
    </form>
</body></html>