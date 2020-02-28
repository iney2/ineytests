Feature: Check information about employees

	Scenario: check of salary
		Given information about employees
		When take salary of Doris Wilder
		Then value of salary is match with expected