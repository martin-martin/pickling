Hi Ian, here's a quick showcase to support my review comments.

The files `f_pickling.py` and `f_unpickling.py` showcase how it's possible to pickle user-defined functions by qualified name, and how you're able to unpickle them as well, as long as the qualified name is accessible to your Python interpreter.

You can get `f_unpickling.py` to work by uncommenting the import at the top.

---

Further, the files `op_pickling.py` and `op_unpickling.py` show a possible example of showcasing how the workflow can be improved using the `operator` module. Here, there's no need to import anything into the global namespace of `op_unpickling.py`, because `pickle` knows about the fully qualified name of `operator.add` and [imports the module](https://github.com/python/cpython/blob/main/Modules/_pickle.c#L7088) (which is readily avaialble because it's a built-in standard library module).

---

This could be a possible progression of showing first why users might run into issues when attempting to pickle a user-defined function, and how using the corresponding function from the `operator` module doesn't run into the same issues.

Alternatively to showing a custom defined function, you could also show a lambda function, which actually can't be pickled at all (`lambdadd.py`).
