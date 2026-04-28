package com.anasttruh.spring_lab3_notifications.repository;

import com.anasttruh.spring_lab3_notifications.model.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
