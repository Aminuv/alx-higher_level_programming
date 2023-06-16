#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - for Printing bytes information
 * @p: Object
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, i, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		limit = 10;
	else
		limit = s + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - for Printing a list for an information
 * @p: Python
 * Return: 0
 */
void print_python_list(PyObject *p)
{
	long int s2, i;
	PyListObject *li;
	PyObject *objs;

	s2 = ((PyVarObject *)(p))->ob_size;
	li = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s2);
	printf("[*] Allocated = %ld\n", li->allocated);

	for (i = 0; i < s2; i++)
	{
		objs = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
