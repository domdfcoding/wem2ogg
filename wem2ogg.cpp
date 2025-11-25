#define PY_SSIZE_T_CLEAN
#include "wwtools/wwtools.hpp"
#include <Python.h>
#include <memory>
#include <string>
#include <vector>

static PyObject *wem_to_ogg(PyObject *self, PyObject *args) {
	char *src;
	Py_ssize_t src_len;

	if (!PyArg_ParseTuple(args, "y#", &src, &src_len)) {
		PyErr_SetString(PyExc_TypeError, "Invalid parameters");
		return NULL;
	}

	std::string indata{src, src_len};
	std::string ogg_data = wwtools::wem_to_ogg(indata);

	if (!ogg_data.length()) {
		PyErr_SetString(PyExc_ValueError, "Error converting wem to ogg");
		return NULL;
	}

	PyObject *pbo = PyBytes_FromStringAndSize(ogg_data.c_str(), ogg_data.length());

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
