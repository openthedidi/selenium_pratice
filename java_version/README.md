# Java Selenium 版本

這個資料夾提供 Python `pytest_POM_demo` 的 Java 對應版本。

## 技術棧
- Java 17
- Maven
- Selenium 4
- JUnit 5
- WebDriverManager

## 專案結構
- `src/main/java/com/example/selenium/config/BrowserFactory.java`
- `src/main/java/com/example/selenium/pages/LoginPage.java`
- `src/test/java/com/example/selenium/tests/LoginTest.java`

## 執行
```bash
cd java_version
mvn test -DbaseUrl=https://your-target-login-page -Dheadless=true
```

> `baseUrl` 預設為 `https://www.google.com`，如未提供正確登入頁面，測試會失敗。
