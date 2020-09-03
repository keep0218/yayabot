# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        # message.content = message의 내용
        if message.content == "야야 안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 안녕하세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "dldl":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "한/영키를 눌러야 제 이름이 뜨죠! 제 이름은 dldl이 아니라 야야에요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 원하는 거 있어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "모두와 같이 오래오래 있는 거요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "이름만 부르면 무슨 말을 하는 지 알 수 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 사랑해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 사랑해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 사랑해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 사랑해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 재밌다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "재밌어 해주시니 기분 상쾌해요! 야야는 그러기 위해 있는 로봇이니까요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나 간다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "안녕히주무세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "잘자요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "저 이제 잘게요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "잘게요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "굿나잇":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "좋은밤":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "좋은 밤":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅇㅎㅇ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "어서오세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "어서오세요! 야야는 모든 사람들을 환영해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 끝말잇기":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 주사위":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 마피아":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 음악 재생":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 할 줄 아는 게 뭐야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그렇게 말씀하시면 슬퍼요.. 야야는 여러분과 떠들 수 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아하는 게 뭐야?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 다른 사람들이 좋아하는 걸 좋아해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 싫어하는 게 뭐야?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 다른 사람들이 싫어하는 걸 싫어해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 멍청이":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "욕하지 마세요! 전부 듣고 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 멍청해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "욕하지 마세요! 전부 듣고 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅃㅃ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "바보라고 하는 사람이 더 바보랬어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 뭐해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 이 곳에서 여러분을 반길 준비를 하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 마감":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감해야돼":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감있음":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감해야함":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 다녀올게":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "다녀오세요! 야야는 계속 기다릴거니까 빨리 오세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 이야기해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "옛날옛날에, 아주 먼 옛날 옛적에... 너무 기니까 중간은 생략할게요! ... 오래오래 행복하게 살았답니다! 어? 너무 많이 줄였나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

            # 서버에 멤버가 들어왔을 때 수행 될 이벤트
            async def on_member_join(self, member):
                msg = "<@{}>! 어서오세요! 야야가 쭉 기다리고 있었어요!".format(str(member.id))
                await find_first_channel(member.guild.text_channels).send(msg)
                return None

            # 사버에 멤버가 나갔을 때 수행 될 이벤트
            async def on_member_remove(self, member):
                msg = "<@{}>님이 나갔네요... 다시 만날 수 있으면 좋겠다!".format(str(member.id))
                await find_first_channel(member.guild.text_channels).send(msg)
                return None

            # 반복 작업을 위한 패키지
            from discord.ext import tasks
            # 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
            import datetime
            # 중복 전송을 방지하기 위해 사용할 패키지
            import time
            @tasks.loop(seconds=1)
            async def every_hour_notice(self):
                if datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
                    await client.get_guild("Input Your Server ID as Int").get_channel(
                        "Input Your Channel ID as Int").send(
                        "지금은 {}시 {}분 이에요!".format(datetime.datetime.now().hour, datetime.datetime.now().minute))

                    # 1초 sleep하여 중복 전송 방지
                    time.sleep(1)

        if message.content == "야야 태그해 줘":
            channel = message.channel

            msg = "<@{}>".format(message.author.id)
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
client.run("NzUwOTU5NDYxMDE0ODMxMTE1.X1CHfw.Fp8z65QEniNdx5KFoGt_83kPfdo")
