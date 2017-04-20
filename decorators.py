# -*- coding: utf-8 -*-
def my_first_decorator(func_to_decorate):
    def wrapper_for_func_to_decorate():
        print('_____________________________________________Definition________________________________________________')
        func_to_decorate()
        print('_____________________________________________________________________________________________________ \n')
    return wrapper_for_func_to_decorate


def test_case_print():
    print('A test case, in software engineering, is a set of conditions under which a tester will determine whether \n'
          'an application, software system or one of its features is working as it was originally intended. \n'
          'The mechanism for determining whether a software program or system has passed or failed such a test is \n'
          'known as a test oracle. In some settings, an oracle could be a requirement or use case, while in others it\n'
          'could be a heuristic. It may take many test cases to determine that a software program or system is \n '
          'considered sufficiently scrutinized to be released. Test cases are often referred to as test scripts, \n'
          'particularly when written - when they are usually collected into test suites.')

fancy_decorated = my_first_decorator(test_case_print)
fancy_decorated()

@my_first_decorator
def tp_desc():
    print('Test plan is a document describing the scope,approach, resources and schedule of intended test activities.\n'
          'It identifies amongst others test items,the features to be tested,the testing tasks,who will do each task,\n'
          'degree of tester independence,the test environment, the test design techniques and entry and exit criteria\n'
          ' to be used, and the rationale for their choice,and any risks requiring contingency planning.')

tp_desc()
