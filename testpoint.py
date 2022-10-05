<?xml version="1.0" encoding="utf-8"?><testsuites><testsuite name="pytest" errors="0" failures="2" skipped="0" tests="4" time="0.172" timestamp="2022-10-05T10:04:21.882457" hostname="ubuntu"><testcase classname="test_class.TestClass" name="test_one" time="0.002" /><testcase classname="test_class.TestClass" name="test_two" time="0.002"><failure message="AssertionError: assert False&#10; +  where False = hasattr('hello', 'check')">self = &lt;test_class.TestClass object at 0x7f2920de5910&gt;

    def test_two(self):
        x = "hello"
&gt;       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:9: AssertionError</failure></testcase><testcase classname="test_sample" name="test_answer" time="0.002"><failure message="assert 4 == 5&#10; +  where 4 = func(3)">def test_answer():
&gt;       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:7: AssertionError</failure></testcase><testcase classname="test_sysexit" name="test_mytest" time="0.001" /></testsuite></testsuites>