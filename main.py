import driverGet
import login
import plan_it
import current_request
import notice_it
import inadvance_it

# 크롬 브라우저를 실행 및 초기 로그인 페이지로 이동
driver = driverGet.driver()
driver.get("https://www.g2bplus.kr/member_pclogin.php")



login.login_excute(driver) #로그인
current_request.current(driver) # 조달요청현황 실행
plan_it.plan(driver) # 발주계획(IT) 실행
notice_it.notice(driver) #입찰공고(IT) 실행
inadvance_it.inadvance(driver) #사전규격현황(IT) 실행