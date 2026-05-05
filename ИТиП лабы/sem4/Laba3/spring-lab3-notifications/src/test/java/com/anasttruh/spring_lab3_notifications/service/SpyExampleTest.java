package com.anasttruh.spring_lab3_notifications.service;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class SpyExampleTest {

    @Test
    void shouldUseSpyForPartialMocking() {
        List<String> realList = new ArrayList<>();
        List<String> spyList = spy(realList);

        spyList.add("Spring");
        spyList.add("Boot");

        verify(spyList, times(1)).add("Spring");
        verify(spyList, times(1)).add("Boot");
        verify(spyList, times(2)).add(anyString());

        assertEquals(2, spyList.size());
        assertTrue(spyList.contains("Spring"));
    }

    @Test
    void shouldStubSpecificMethodOnSpy() {
        List<String> spyList = spy(new ArrayList<>());

        doReturn("mocked").when(spyList).get(0);

        spyList.add("real");
        assertEquals("mocked", spyList.get(0));
        verify(spyList).get(0);
    }
}