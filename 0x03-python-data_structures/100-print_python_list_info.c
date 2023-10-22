#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	long int size, alloc, i;
	PyObject *item;
	PyListObject *list;

	size = PyList_Size(p);
	list = (PyListObject *)p;
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
