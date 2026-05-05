package com.anasttruh.spring_lab3_notifications.controller;

import com.anasttruh.spring_lab3_notifications.model.dto.NotificationDto;
import com.anasttruh.spring_lab3_notifications.model.entity.Notification;
import com.anasttruh.spring_lab3_notifications.model.entity.User;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationChannel;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationStatus;
import com.anasttruh.spring_lab3_notifications.security.JwtService;
import com.anasttruh.spring_lab3_notifications.service.NotificationService;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDateTime;
import java.util.List;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import org.springframework.boot.test.mock.mockito.MockBean;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(NotificationController.class)
@AutoConfigureMockMvc(addFilters = false) // отключаем security filters
class NotificationControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private JwtService jwtService;

    @MockBean
    private NotificationService notificationService;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    void shouldReturnOkForGetAllNotifications() throws Exception {
        when(notificationService.getAllNotifications()).thenReturn(List.of());

        mockMvc.perform(get("/notifications/all"))
                .andExpect(status().isOk());
    }

    @Test
    void shouldReturnNotificationById() throws Exception {
        User user = new User();
        user.setId(1L);

        Notification notification = new Notification();
        notification.setId(1L);
        notification.setTitle("Тест");
        notification.setMessage("Сообщение");
        notification.setChannel(NotificationChannel.EMAIL);
        notification.setStatus(NotificationStatus.CREATED);
        notification.setCreatedAt(LocalDateTime.now());
        notification.setRecipient(user);

        when(notificationService.getNotificationById(1L))
                .thenReturn(notification);

        mockMvc.perform(get("/notifications/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("Тест"))
                .andExpect(jsonPath("$.message").value("Сообщение"));
    }

    @Test
    void shouldCreateNotification() throws Exception {
        NotificationDto request = NotificationDto.builder()
                .title("Новое")
                .message("Текст")
                .channel(NotificationChannel.PUSH)
                .recipientId(1L)
                .build();

        User user = new User();
        user.setId(1L);

        Notification savedNotification = new Notification();
        savedNotification.setId(5L);
        savedNotification.setTitle("Новое");
        savedNotification.setMessage("Текст");
        savedNotification.setChannel(NotificationChannel.PUSH);
        savedNotification.setStatus(NotificationStatus.CREATED);
        savedNotification.setCreatedAt(LocalDateTime.now());
        savedNotification.setRecipient(user);

        when(notificationService.createNotification(any(NotificationDto.class)))
                .thenReturn(savedNotification);

        mockMvc.perform(post("/notifications/add")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(request)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("Новое"))
                .andExpect(jsonPath("$.message").value("Текст"));
    }

    @Test
    void shouldDeleteNotification() throws Exception {
        mockMvc.perform(delete("/notifications/1"))
                .andExpect(status().isOk())
                .andExpect(content().string("Уведомление удалено"));
    }
}