package com.example.selenium.tests;

import com.example.selenium.config.BrowserFactory;
import com.example.selenium.pages.LoginPage;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;

public class LoginTest {

    private WebDriver driver;
    private final String baseUrl = System.getProperty("baseUrl", "https://www.google.com");

    @BeforeEach
    void setUp() {
        boolean headless = Boolean.parseBoolean(System.getProperty("headless", "true"));
        driver = BrowserFactory.createChrome(headless);
        driver.manage().timeouts().implicitlyWait(java.time.Duration.ofSeconds(10));
    }

    @AfterEach
    void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    void validLogin() {
        driver.get(baseUrl);
        LoginPage page = new LoginPage(driver);

        page.enterUsername("admin");
        page.enterPassword("admin1234");
        page.clickLogin();

        Assertions.assertEquals("管理者", page.getSuccessUser());
    }

    @Test
    void invalidLogin() {
        driver.get(baseUrl);
        LoginPage page = new LoginPage(driver);

        page.enterUsername("admin123");
        page.enterPassword("adm");
        page.clickLogin();

        Assertions.assertEquals("ErrorCode:[100]:查無使用者資料", page.getErrorMessage());
    }
}
