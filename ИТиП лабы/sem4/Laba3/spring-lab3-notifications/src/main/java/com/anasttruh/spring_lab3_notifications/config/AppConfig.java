package com.anasttruh.spring_lab3_notifications.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.anasttruh.spring_lab3_notifications")
public class AppConfig {
    // Бины создаются автоматически благодаря сканированию компонентов
}
