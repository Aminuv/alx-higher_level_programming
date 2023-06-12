#include <Python.h>

/**
 * print_python_list_info - For Function that Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int _size, alc, i;
	PyObject *obj;

	_size = Py_SIZE(p);
	alc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", _size);
	printf("[*] Allocated = %d\n", alc);

	for (i = 0; i < _size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
