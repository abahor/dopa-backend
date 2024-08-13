# Admin

/new-question

params = json

text = question text
a = choice a
b = choice b
c = choice c
d = choice d
right = the right answer (a, b, c, d)
chapter = the chapter at the book
subject = subject 
module = module


/delete-question/<int:i>

i = id of the question


/practice/<chap>/<mod>/<sub>

chap = chapter of the book
mod = module
sub = subject

return all question on the is subject


format =
{
            "chapter": i.chapter,
            "subject": i.subject,
            "module": i.module,
            "a": i.a,
            "b": i.b,
            "c": i.c,
            "d": i.d,
            "right": i.right,
            "text": i.text
}


/exam/<chap>/<mod>/<sub>

chap = chapter of the book
mod = module
sub = subject

return 10 question on the is subject


format =
{
            "chapter": i.chapter,
            "subject": i.subject,
            "module": i.module,
            "a": i.a,
            "b": i.b,
            "c": i.c,
            "d": i.d,
            "right": i.right,
            "text": i.text
}
