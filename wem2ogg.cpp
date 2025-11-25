#define PY_SSIZE_T_CLEAN
#include "wwtools/wwtools.hpp"
#include <Python.h>
#include <memory>
#include <string>
#include <vector>

static PyObject *wem_to_ogg(PyObject *self, PyObject *args) {
	unsigned char *src;
	Py_ssize_t src_len;

	if (!PyArg_ParseTuple(args, "y#", &src, &src_len)) {
		PyErr_SetString(PyExc_TypeError, "Invalid parameters");
		return NULL;
	}

	std::string indata((char *)src);
	std::string ogg_data = wwtools::wem_to_ogg(indata);

	PyObject *pbo = PyBytes_FromString(ogg_data.c_str());

	return pbo;
}

static PyMethodDef methods[] = {
	{"wem_to_ogg", (PyCFunction)wem_to_ogg, METH_VARARGS, NULL},
	{NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
	PyModuleDef_HEAD_INIT, "wem2ogg", NULL, -1, methods,
};

PyMODINIT_FUNC PyInit_wem2ogg(void) { return PyModule_Create(&module); }
