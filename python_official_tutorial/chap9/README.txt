A namespaces is a mapping from names to objects.

The important thing to know about namespaces is that there
is absolutely no relation between names in different namespaces;
for instance, two namespaces is that there is absolutely no relation
between names in different namespaces; for instance, two different modules
may both define a function maximize without confusion -- users of the modules
must prefix it with the module name.



class definitions, like function definitions (def statements) must be executed
before they have any effect. (You could conceivably place a class definition in a branch of
an if statement, or inside a function.)

Class objects support two kinds of operations: 
attribute references and instantiation.

Attribute references use the standard syntax used for all attribute references
in Python: obj.name. Valid attribute names are all the names that were
in the class's namespace when the class object was created.


self:
Often, the first argument of a method is called self. This is nothing more than a convention:
the name self has absolutely no special meaning to Python. Note, however, that
by not following the convention your code may be less readable to other Python programmers,
and it is also conceivable that a class browser program might be written that relies upon
such a convention.
