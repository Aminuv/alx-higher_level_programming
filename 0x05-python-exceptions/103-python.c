#include <Python.h>

void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print basic of python list .
 * @p: the PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *itm;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			itm = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, itm->ob_type->tp_name);
			if (PyBytes_Check(itm))
				print_python_bytes(itm);
			else if (PyFloat_Check(itm))
				print_python_float(itm);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_float - print basics in the  data of the PyFloatObject
 * @p: the PyObject float
 */
void print_python_float(PyObject *p)
{
	double v = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - Prints basic in the data of  Python byte objects.
 * @p: the PyObject list
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}
