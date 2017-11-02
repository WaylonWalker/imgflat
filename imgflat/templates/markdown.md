# {{ directory }}

{% for file in files %}
## {{ file }}
![{{file}}][{{file}}]
{% endfor %}
<!-- images -->
{% for file in files %}
[{{ file }}]:data:image/png;base64,{{ files[file].replace("b'", '').replace("'", '') }}
{% endfor %}