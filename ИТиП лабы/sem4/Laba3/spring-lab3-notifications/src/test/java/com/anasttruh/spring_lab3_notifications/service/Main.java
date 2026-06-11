package com.anasttruh.spring_lab3_notifications.service;

import java.time.LocalDate;
import java.time.DayOfWeek;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class Main {

    record Employee(String name, int daysWorked) {}

    public static void main(String[] args) {
        List<Employee> staff = List.of(
                new Employee("Иван Иванов", 993),
                new Employee("Пётр Петров", 994),
                new Employee("Алексей Сидоров", 995),
                new Employee("Дмитрий Смирнов", 999),
                new Employee("Сергей Кузнецов", 1000),
                new Employee("Никита Попов", 1001),
                new Employee("Андрей Васильев", 1993),
                new Employee("Михаил Новиков", 1994),
                new Employee("Владимир Фёдоров", 1995),
                new Employee("Егор Морозов", 1996),
                new Employee("Максим Волков", 2000),
                new Employee("Роман Алексеев", 2001),
                new Employee("Артём Лебедев", 2002),
                new Employee("Кирилл Семёнов", 2005),
                new Employee("Олег Егоров", 2006),
                new Employee("Иван Петров", 2007),
                new Employee("Пётр Иванов", 200) // Значение оставлено как в исходных данных
        );

        final int START_MILESTONE = 1000;
        final int STEP = 1000;
        final LocalDate TODAY = LocalDate.of(2026, 5, 19);
        final LocalDate WEEK_START = TODAY.with(DayOfWeek.MONDAY);
        final LocalDate WEEK_END = WEEK_START.plusDays(6);
        final DateTimeFormatter DATE_FORMAT = DateTimeFormatter.ofPattern("dd.MM");

        String[][] result = staff.stream()
                .filter(emp -> emp.daysWorked() >= START_MILESTONE)
                .map(emp -> {
                    int stepsPassed = (emp.daysWorked() - START_MILESTONE) / STEP;
                    int nextMilestone = START_MILESTONE + (stepsPassed + 1) * STEP;
                    int daysUntilMilestone = nextMilestone - emp.daysWorked();
                    return new Object[]{emp, nextMilestone, daysUntilMilestone};
                })
                .filter(data -> {
                    LocalDate targetDate = TODAY.plusDays((int) data[2]);
                    return !targetDate.isBefore(WEEK_START) && !targetDate.isAfter(WEEK_END);
                })
                .sorted(Comparator.comparingInt(data -> (int) data[2]))
                .map(data -> new String[]{
                        TODAY.plusDays((int) data[2]).format(DATE_FORMAT),
                        ((Employee) data[0]).name() + " – " + data[1] + " дней"
                })
                .toArray(String[][]::new);

        System.out.println("Date\tText");
        Arrays.stream(result).forEach(row -> System.out.println(row[0] + "\t" + row[1]));
    }
}
