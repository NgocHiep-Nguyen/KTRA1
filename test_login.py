import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Fixture setup trình duyệt chạy 1 lần cho các test case
@pytest.fixture(scope="module")
def driver():
    print("Khởi tạo Chrome...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("Đóng Chrome...")
    driver.quit()

@allure.epic("Văn phòng điện tử UTC")
@allure.feature("Chức năng Đăng nhập")
class TestLoginUTC:

    # @allure.story("Đăng nhập thành công")
    # @allure.title("TC_01: Đăng nhập với tài khoản và mật khẩu hợp lệ")
    # def test_login_success(self, driver):
    #     with allure.step("1. Mở trang đăng nhập"):
    #         driver.get("https://vanphongdientu.utc.edu.vn/Login")
    #         time.sleep(2)
        
    #     with allure.step("2. Nhập thông tin tài khoản"):
    #         # Lấy chính xác name="username" từ HTML
    #         txt_username = driver.find_element(By.NAME, "username") 
    #         txt_username.clear()
    #         txt_username.send_keys("9999999999") 
            
    #     # Lấy chính xác name="userpwd" từ HTML
    #         txt_password = driver.find_element(By.NAME, "userpwd")
    #         txt_password.clear()
    #         txt_password.send_keys("123456")
    #         time.sleep(1)
        
    #     with allure.step("3. Click nút Đăng nhập"):
    #         # Lấy chính xác class="submit_login" từ HTML
    #         driver.find_element(By.CLASS_NAME, "submit_login").click()
    #         time.sleep(4)
            
    #     with allure.step("4. Kiểm tra kết quả chuyển hướng"):
    #         # Nếu URL không còn chứa chữ Login tức là đã vào được hệ thống
    #         assert "Login" not in driver.current_url, "Lỗi: Vẫn đang ở trang Login, đăng nhập thất bại!"
    # @allure.story("Đăng nhập bằng Email")
    # @allure.title("TC_05: Kiểm tra chuyển hướng Đăng nhập bằng Email")
    # def test_redirect_google_login(self, driver):
    #     with allure.step("1. Mở trang đăng nhập"):
    #         driver.get("https://vanphongdientu.utc.edu.vn/Login")
    #         time.sleep(2)
        
    #     with allure.step("2. Click nút 'Đăng nhập bằng e-mail UTC'"):
    #         # Tìm nút đăng nhập email dựa vào đoạn text của thẻ <a>
    #         btn_google_login = driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập bằng e-mail")
    #         btn_google_login.click()
            
    #         # Đợi một chút để mạng load sang trang Google
    #         time.sleep(3)
            
    #     with allure.step("3. Kiểm tra kết quả chuyển hướng"):
    #         current_url = driver.current_url
            
    #         # Kiểm tra xem URL hiện tại có chứa miền của Google xác thực không
    #         assert "accounts.google.com" in current_url, f"Lỗi: Không chuyển hướng đến Google. URL hiện tại: {current_url}"
            
    #         # Ghi chú trực tiếp vào báo cáo Allure về việc Google chặn Selenium
    #         allure.attach("Google thường chặn đăng nhập từ Selenium do chính sách bảo mật, tuy nhiên việc chuyển hướng (Redirect) đã diễn ra thành công.", name="Lưu ý bảo mật", attachment_type=allure.attachment_type.TEXT)
    @allure.story("Đăng nhập thành công")
    @allure.title("TC_08: Đăng nhập sử dụng phím Enter")
    def test_login_with_enter_key(self, driver):
        with allure.step("1. Mở trang đăng nhập"):
            driver.get("https://vanphongdientu.utc.edu.vn/Login")
            time.sleep(2)
        
        with allure.step("2. Nhập thông tin tài khoản và mật khẩu"):
            txt_username = driver.find_element(By.NAME, "username") 
            txt_username.clear()
            txt_username.send_keys("6451071023") 
            
            txt_password = driver.find_element(By.NAME, "userpwd")
            txt_password.clear()
            txt_password.send_keys("Ngochiep") # Bạn nhớ thay bằng mật khẩu thật nếu cần
            time.sleep(1)
        
        with allure.step("3. Nhấn phím Enter thay vì click nút Đăng nhập"):
            # Truyền phím ENTER trực tiếp vào ô mật khẩu
            txt_password.send_keys(Keys.ENTER)
            time.sleep(4) # Đợi hệ thống xử lý đăng nhập
            
        with allure.step("4. Kiểm tra kết quả chuyển hướng"):
            # Nếu URL không còn chữ Login tức là đã vào được hệ thống thành công
            assert "Login" not in driver.current_url, "Lỗi: Không thể đăng nhập bằng phím Enter!"