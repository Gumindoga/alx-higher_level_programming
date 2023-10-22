#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

void print_python_bytes(PyObject *p)
{
	long int size;
	char *trying_str;
	unsigned char *bytes_str;
	long int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	trying_str = PyBytes_AsString(p);
	bytes_str = (unsigned char *)trying_str;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", trying_str);

	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i < size + 1 && i < 10; i++)
		printf(" %02hhx", bytes_str[i]);

	printf("\n");
}
