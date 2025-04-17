from RagLlm import response_

if __name__ == "__main__":
    while True:
        user_input = input("\nAsk a question (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        response = response_(user_input)

        print("\nResponse:\n", response)
