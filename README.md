plain-failed
============

Python script to get a plain list of only the failing tests out of Jenkins json test report url

----

You know, those days when a new feature is introduced and the next day your Jenkins dashboard is yellow as the sun?
Well sometimes, it happens and those days I want to get a plain list of issues, in order to group the tests per type of failures.

If you're lazy like me, you don't wanna click on every failing test to see the error details and possible claims.

So there comes the script :)

NB: it uses the urllib2 lib so it won't work in Python 3
