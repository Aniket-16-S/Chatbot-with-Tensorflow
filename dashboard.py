import streamlit as st
import json
from streamlit.web import cli
from streamlit import runtime
import sys

#Reads queries (all)
def read() :
    try :
        with open("unsolved.json", 'r+') as file :
            dic = json.load(file)
            lst = dic['unA']          
    except FileNotFoundError :
        lst = []
        
    return lst

# writes queries back to unsolved.json Except given queries in lst
def write(lst = []) :
    curent = read()
    new = [q for q in curent if q not in lst]
    print(new)
    with open("unsolved.json", 'w') as file :
        json.dump({'unA' : new}, file)

def modefy_train_set(t_q_a_list):
    if t_q_a_list:
        with open("faq.json", 'r+', encoding='utf-8') as file:
            data = json.load(file)
            if 'intents' not in data:
                data['intents'] = []
            data['intents'].extend(t_q_a_list)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()



st.markdown("### Unanswered Queries :")

unanswered_queries = read()
if unanswered_queries:

    with st.form("answer_form"):
        st.write("Please provide answers and relevent tags for the following queries:")
        st.markdown("#### You can type * in place of ansers to delete the query.")
        answered_data = [] 

        for i, query in enumerate(unanswered_queries):
            st.markdown(f"### {i+1} {query} :")
            tg = st.text_area(f"Tag : ", placeholder = "Enter catagory /  tag for this question.", key = f"tag{i}")
            
            answer = st.text_area(f"Your Answer for '{query}':", key = f"ans{i}" , placeholder ="type Answer here. Use # for multiple answers.").strip().split('#')
            
            answered_data.append({"tag" : tg, "query": query, "answer": answer})

        submit_button = st.form_submit_button("Submit All Answers")

        if submit_button:
            successfully_answered_queries = []
            edy = []
            for item in answered_data:
                query = item["query"]
                answer = item["answer"]
                tag = item["tag"] if item["tag"] != '' else query
                if answer != [''] :
                    if answer != ['*'] and tag != '*':
                        successfully_answered_queries.append({"tag" : tag , "patterns" : [query], "responses" : answer})
                    edy.append(query)
                    st.success(f"Answered '{query}' with: {answer}")
                else:
                    st.warning(f"No answer provided for: {query}")
            
            if successfully_answered_queries or edy:
                write(edy)
                modefy_train_set(successfully_answered_queries)
                st.rerun() 
            else:
                st.info("No new answers submitted.")

else:
    st.success("All queries answered! Great job!")

def open_dashB() :
    if not runtime.exists() :
        sys.argv = ["streamlit", "run", "dashboard.py"]
        cli.main()

if __name__ == '__main__' :
    open_dashB()