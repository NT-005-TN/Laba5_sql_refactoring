package com.anasttruh.spring_lab3_notifications.service;

import com.anasttruh.spring_lab3_notifications.model.dto.NotificationDto;
import com.anasttruh.spring_lab3_notifications.model.entity.Notification;
import com.anasttruh.spring_lab3_notifications.model.entity.User;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationChannel;
import com.anasttruh.spring_lab3_notifications.model.enums.NotificationStatus;
import com.anasttruh.spring_lab3_notifications.repository.NotificationRepository;
import com.anasttruh.spring_lab3_notifications.repository.UserRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class NotificationServiceTest {

    @Mock
    private NotificationRepository notificationRepository;

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private NotificationService notificationService;

    @Test
    void shouldGetNotificationById() {
        User user = new User();
        user.setId(1L);

        Notification notification = new Notification();
        notification.setId(10L);
        notification.setTitle("Тестовое уведомление");
        notification.setRecipient(user);

        when(notificationRepository.findById(10L)).thenReturn(Optional.of(notification));

        Notification result = notificationService.getNotificationById(10L);

        assertNotNull(result);
        assertEquals(10L, result.getId());
        assertEquals("Тестовое уведомление", result.getTitle());
        verify(notificationRepository, times(1)).findById(10L);
    }

    @Test
    void shouldThrowExceptionWhenNotificationNotFound() {
        when(notificationRepository.findById(999L)).thenReturn(Optional.empty());

        assertThrows(RuntimeException.class, () -> notificationService.getNotificationById(999L));
        verify(notificationRepository, times(1)).findById(999L);
    }

    @Test
    void shouldCreateNotificationWithValidData() {
        User recipient = new User();
        recipient.setId(1L);

        NotificationDto dto = NotificationDto.builder()
                .title("Заголовок")
                .message("Сообщение")
                .channel(NotificationChannel.EMAIL)
                .recipientId(1L)
                .build();

        Notification savedNotification = new Notification();
        savedNotification.setId(5L);
        savedNotification.setTitle(dto.getTitle());
        savedNotification.setRecipient(recipient);

        when(userRepository.findById(1L)).thenReturn(Optional.of(recipient));
        when(notificationRepository.save(any(Notification.class))).thenReturn(savedNotification);

        Notification result = notificationService.createNotification(dto);

        assertNotNull(result);
        assertEquals("Заголовок", result.getTitle());
        assertEquals(NotificationStatus.CREATED, result.getStatus());
        verify(userRepository, times(1)).findById(1L);
        verify(notificationRepository, times(1)).save(any(Notification.class));
    }
}