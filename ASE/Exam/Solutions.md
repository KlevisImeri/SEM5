```java
class Authors {
    Affiliations[0..*] affiliations;
}
abstract class Affiliations {}
class University extends Affiliations {
    City[1] city;
    contains Faculty[1..*] faculties;
}
class Faculty extends Affiliations {
    contains Department[1..20] departments;
}
class Department extends Affiliations {}
class City {}
class Publications {
    Authors[1..*] authors;
    Publications[0..*] cites;
}
class ConferencePaper extends Publications {
   Conference[1] presentedAt;
}  
class JournalPaper extends Publications {
    Issue[1] appearsIn;
}
class Conference {
    City[1] heldIn;
}
class Journal { 
    contains Issue[1..*] issues;
}
class Issue{}
```

Simple:
```
{%- for pub in database.publications %}
@article{ {{ pub.name }},
  title={ {{- pub.title -}} },
  author={
    {%- for a in pub.authors -%}
    {{a}}{%if not loop.last %} and {%endif%}
    {%- endfor -%}
  },
  pages={ {{- pub.fromPages}}--{{ pub.toPages -}}}
  year={ {{- pub.year -}}}
},
{% endfor %}
```

Full:
```
{%- for pub in database.publications %}
@article{ {{ pub.name }},
  title={ {{- pub.title -}} },
  author={
    {%- for a in pub.authors -%}
    {{a}}{%if not loop.last %} and {%endif%}
    {%- endfor -%}
  },
  {%- if pub.journal %}
  journal={ {{-pub.journal-}} },
  {%- endif %}
  {%- if pub.fromPages and pub.toPages %}
  pages={ {{- pub.fromPages }}--{{ pub.toPages }}},
  {%- else %}
  {%- if pub.pp%}
  paragraph= { {{-pub.pp-}} },
  {%- endif %}
  {%- endif %}
  year={ {{- pub.year -}} },
},
{% endfor %}
```

Test:
```yaml
database:
  authors:
    - name: "Alice"
    - name: "Bob"
    - name: "Sara"
  journals:
    - name: "Science"
    - name: "Nature"
  publications:
    - name: "j1"
      authors:
        - "Alice"
        - "Bob"
        - "Sara"
      year: 2024
      title: "Exploring the Universe"
      journal: "Science"
    - name: "j2"
      authors:
        - "Bob"
      year: 2023
      title: "Quantum Mechanics"
      journal: "Nature"
      fromPages: 101
      toPages: 120
    - name: "j3"
      authors:
        - "Alice"
        - "Bob"
      year: 2024
      title: "Exploring Quantum Theory"
      journal: "Science"
      pp: 101
    - name: "j4"
      authors:
        - "Bob"
      year: 2023
      title: "New Discoveries in Physics"
      journal: "Nature"
```