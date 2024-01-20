#include <object.h>
#include <listobject.h>
#include <python.h>

/**
 * print_python_list_info - Prints Basic Information about Python Lists
 * @p: The List
 */
void print_python_list_info(PyObject *p)
{
	int elm;

	printf("[*] Size of the Python List = %lu\n", Py_Sie(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elm = 0; elm < Py_Size(p); elm++)
		printf("Element %d: %s\n", elm, Py_Type(PyList_Getitem(p, elm))>tp_name);
}
