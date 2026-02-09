package com.example.selenium.config;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class BrowserFactory {

    private BrowserFactory() {
    }

    public static WebDriver createChrome(boolean headless) {
        WebDriverManager.chromedriver().setup();

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--lang=zh-TW");
        options.addArguments("--disable-notifications");
        options.addArguments("--window-size=1920,1080");

        if (headless) {
            options.addArguments("--headless=new");
            options.addArguments("--disable-gpu");
        }

        return new ChromeDriver(options);
    }
}
