🔥 Main Difference
👉 course_pk
Just a number from the URL
Not an object

Comes from this:

/course/1/
👉 course.pk
Comes from a Course object
It is the ID of that object from database


✅ 1. course.pk (first template)
{% url 'quiz' course.pk quiz.pk %}

👉 Here you already have:

{{ course.title }}

So:

✔ course = full Course object
✔ course.pk = ID from that object

💡 Meaning:

“I already have the course object, so I take its ID”

✅ 2. course_pk (second template)
{% url 'quiz' course_pk next_quiz.pk %}

👉 Here you do NOT have course object in template
👉 You only passed:

course_pk = some number