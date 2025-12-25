import React, { useState, useEffect } from 'react';
import { 
  Terminal, 
  Cpu, 
  Gamepad2, 
  MessageSquare, 
  Code2, 
  Zap, 
  Globe, 
  User, 
  Settings, 
  ExternalLink,
  Github,
  Linkedin,
  Mail,
  Send,
  Loader2,
  Sparkles,
  Shield,
  Trophy,
  Sword,
  Wand2,
  Activity,
  Box,
  BrainCircuit,
  Binary,
  Layers,
  BarChart3,
  Flame
} from 'lucide-react';

const apiKey = ""; // Gemini API Key provided by the environment

const App = () => {
  const [activeTab, setActiveTab] = useState('profile');
  const [isBooting, setIsBooting] = useState(true);
  const [input, setInput] = useState("");
  const [chatHistory, setChatHistory] = useState([
    { role: "ai", text: "Neural Link Established. System authorized for user: Amit Kumar. Core AI/ML modules active. How can I assist you today?" }
  ]);
  const [isTyping, setIsTyping] = useState(false);
  
  // Amit's Personal Data (Updated for Professional/AI theme)
  const profile = {
    name: "Amit Kumar",
    class: "AI/ML Engineer & Full Stack Architect",
    level: "Core V2.0",
    server: "Patna, India",
    guild: "Govt. Polytechnic Barh",
    leetcode: "Amitkumar2801",
    parameters: [
      { name: "Algorithmic Logic", level: 98, icon: <Binary size={14}/> },
      { name: "Neural Sync (Soft Skills)", level: 95, icon: <Layers size={14}/> },
      { name: "Execution Speed", level: 88, icon: <Zap size={14}/> },
      { name: "System Optimization", level: 92, icon: <Activity size={14}/> }
    ]
  };

  const inventory = {
    languages: ["Python", "JavaScript", "C", "SQL"],
    frameworks: ["React", "NestJS", "Next.js", "Tailwind"],
    ai_ml: ["Pandas", "NumPy", "Scikit-Learn", "Deep Learning"],
    dev_ops: ["Git", "Docker", "MySQL", "AWS Shell"]
  };

  const quests = [
    { title: "AI/ML Intern", org: "Infosys Springboard 3.0", status: "STABLE_DEPLOY", color: "text-green-400" },
    { title: "ML Intern", org: "NIELIT Patna", status: "STABLE_DEPLOY", color: "text-green-400" },
    { title: "Diploma: AI/ML", org: "Govt. Poly. Barh", status: "COMPILING...", color: "text-cyan-400" }
  ];

  useEffect(() => {
    const timer = setTimeout(() => setIsBooting(false), 2000);
    return () => clearTimeout(timer);
  }, []);

  const callGemini = async (prompt) => {
    let delay = 1000;
    for (let i = 0; i < 5; i++) {
      try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            systemInstruction: { parts: [{ text: `You are the onboard AI for Amit Kumar's professional terminal. User info: ${JSON.stringify(profile)}. Be concise, highly professional, and use AI/Engineering terminology. Speak only in English.` }] }
          })
        });
        if (!response.ok) throw new Error('API Error');
        const data = await response.json();
        return data.candidates?.[0]?.content?.parts?.[0]?.text;
      } catch (error) {
        if (i === 4) return "Neural uplink error. Check connection.";
        await new Promise(res => setTimeout(res, delay));
        delay *= 2;
      }
    }
  };

  const handleChat = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    const msg = input;
    setInput("");
    setChatHistory(prev => [...prev, { role: "user", text: msg }]);
    setIsTyping(true);
    const aiRes = await callGemini(msg);
    setChatHistory(prev => [...prev, { role: "ai", text: aiRes }]);
    setIsTyping(false);
  };

  if (isBooting) {
    return (
      <div className="min-h-screen bg-[#020202] flex flex-col items-center justify-center p-4">
        <div className="w-48 h-1 bg-gray-900 rounded-full overflow-hidden relative">
          <div className="absolute inset-0 bg-cyan-500 w-full animate-[slide_1.5s_infinite]"></div>
        </div>
        <div className="mt-4 font-mono text-[10px] text-cyan-500 tracking-[0.4em] uppercase">
          Synthesizing_Core_Kernel
        </div>
        <style>{`@keyframes slide { from { transform: translateX(-100%); } to { transform: translateX(100%); } }`}</style>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#050505] text-slate-300 font-sans p-3 md:p-8 selection:bg-cyan-500/30">
      {/* HUD Background elements */}
      <div className="fixed inset-0 pointer-events-none opacity-20">
        <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_2px_2px,_#ffffff10_1px,_transparent_0)] bg-[size:40px_40px]"></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-500/5 blur-[120px] rounded-full"></div>
      </div>

      <div className="max-w-6xl mx-auto relative z-10">
        {/* Main Command Bar */}
        <header className="grid grid-cols-1 md:grid-cols-12 gap-6 mb-10">
          <div className="md:col-span-8 flex items-center gap-6 bg-white/[0.03] border border-white/10 p-5 rounded-[2.5rem] backdrop-blur-3xl shadow-2xl">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-700 p-[2px] shadow-[0_0_20px_rgba(6,182,212,0.3)]">
              <div className="w-full h-full bg-black rounded-[14px] flex items-center justify-center text-cyan-400 font-black text-2xl">AK</div>
            </div>
            <div>
              <h1 className="text-white font-black text-xl tracking-tight uppercase">Amit_Kumar <span className="text-[10px] text-cyan-500/60 font-mono ml-2 tracking-widest">Protocol.4.0</span></h1>
              <div className="flex gap-4 mt-1 text-[10px] font-mono text-slate-500 uppercase tracking-tighter">
                <span className="flex items-center gap-1 text-cyan-400/70"><Cpu size={10}/> AI_ML_ARCHITECT</span>
                <span className="flex items-center gap-1"><Activity size={10}/> STABILITY_OPTIMAL</span>
                <span className="flex items-center gap-1"><Globe size={10}/> Patna_Node</span>
              </div>
            </div>
          </div>

          <nav className="md:col-span-4 flex items-center justify-center bg-white/[0.03] border border-white/10 p-2 rounded-[2rem] backdrop-blur-3xl">
            {['profile', 'engine', 'neural'].map((tab) => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`flex-1 py-3 rounded-2xl text-[10px] font-black uppercase tracking-[0.2em] transition-all duration-500 ${
                  activeTab === tab ? 'bg-cyan-500 text-black shadow-lg shadow-cyan-500/20' : 'hover:bg-white/5 text-slate-500'
                }`}
              >
                {tab}
              </button>
            ))}
          </nav>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          {/* System Info Sidebar */}
          <aside className="lg:col-span-4 space-y-6">
            <div className="bg-white/[0.03] border border-white/10 rounded-[3rem] p-8 backdrop-blur-3xl relative overflow-hidden group">
              <div className="absolute top-0 right-0 p-4 opacity-[0.03] pointer-events-none group-hover:opacity-[0.07] transition-opacity">
                <BrainCircuit size={150}/>
              </div>
              
              <h3 className="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em] mb-8 border-b border-white/5 pb-4">Engine_Parameters</h3>
              
              <div className="space-y-6">
                {profile.parameters.map(param => (
                  <div key={param.name} className="space-y-2">
                    <div className="flex justify-between items-center text-[9px] font-black uppercase tracking-widest text-slate-400">
                      <span className="flex items-center gap-2">{param.icon} {param.name}</span>
                      <span className="text-cyan-400">{param.level}%</span>
                    </div>
                    <div className="h-1 bg-white/5 rounded-full overflow-hidden">
                      <div className="h-full bg-gradient-to-r from-cyan-500 to-blue-600 rounded-full transition-all duration-1000" style={{ width: `${param.level}%` }}></div>
                    </div>
                  </div>
                ))}
              </div>

              <div className="mt-10 p-4 bg-cyan-500/5 border border-cyan-500/10 rounded-2xl">
                 <div className="flex items-center justify-between mb-2">
                    <span className="text-[9px] font-black text-cyan-400 uppercase tracking-widest flex items-center gap-2"><Flame size={12}/> LeetCode_Rank</span>
                    <a href="https://leetcode.com/u/Amitkumar2801/" target="_blank" className="text-white hover:text-cyan-400 transition-colors"><ExternalLink size={10}/></a>
                 </div>
                 <div className="text-sm font-black text-white">{profile.leetcode}</div>
                 <div className="text-[9px] text-slate-500 mt-1 uppercase">Top Algorithmic Performance</div>
              </div>
            </div>

            <div className="grid grid-cols-3 gap-4">
              <a href="https://www.linkedin.com/in/amit-kumar-835a73345/" target="_blank" className="bg-white/5 border border-white/5 py-4 rounded-3xl flex items-center justify-center hover:bg-[#0A66C2] transition-all hover:scale-110 group">
                <Linkedin size={20} className="group-hover:text-white"/>
              </a>
              <a href="https://github.com/Amitkumar2801" target="_blank" className="bg-white/5 border border-white/5 py-4 rounded-3xl flex items-center justify-center hover:bg-white transition-all hover:scale-110 group">
                <Github size={20} className="group-hover:text-black"/>
              </a>
              <a href="mailto:amitkumar.gpb.ai@gmail.com" className="bg-white/5 border border-white/5 py-4 rounded-3xl flex items-center justify-center hover:bg-[#EA4335] transition-all hover:scale-110 group">
                <Mail size={20} className="group-hover:text-white"/>
              </a>
            </div>
          </aside>

          {/* Main Processing View */}
          <main className="lg:col-span-8">
            <div className="bg-white/[0.03] border border-white/10 rounded-[3rem] h-full min-h-[600px] backdrop-blur-3xl overflow-hidden flex flex-col shadow-2xl">
              
              {activeTab === 'profile' && (
                <div className="p-10 space-y-10 animate-in fade-in slide-in-from-bottom-6 duration-700">
                  <section>
                    <div className="flex items-center gap-3 mb-6">
                      <div className="w-1 h-1 bg-cyan-500 rounded-full"></div>
                      <span className="text-[10px] font-black text-cyan-500 uppercase tracking-[0.4em]">Executive_Summary</span>
                    </div>
                    <h2 className="text-5xl font-black text-white tracking-tighter leading-[0.9] mb-8 uppercase">
                      Pioneering <br/>
                      <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-600">Cognitive Systems.</span>
                    </h2>
                    <p className="text-slate-400 text-sm leading-relaxed max-w-2xl font-medium">
                      Bridging the gap between raw datasets and autonomous logic. Specializing in AI/ML architectures 
                      with a focus on high-performance neural skill matching and full-stack integration. 
                      Currently engineering advanced solutions at GP Barh.
                    </p>
                  </section>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="p-6 bg-white/5 border border-white/5 rounded-[2rem] hover:border-cyan-500/20 transition-all group">
                       <BarChart3 className="text-cyan-500 mb-4 group-hover:scale-110 transition-transform"/>
                       <h4 className="text-white font-bold text-xs uppercase mb-1">Algorithmic Mastery</h4>
                       <p className="text-[10px] text-slate-500 leading-relaxed italic">"Debugging is a tactical operation." 500+ logic hours logged.</p>
                    </div>
                    <div className="p-6 bg-white/5 border border-white/5 rounded-[2rem] hover:border-blue-500/20 transition-all group">
                       <Layers className="text-blue-500 mb-4 group-hover:scale-110 transition-transform"/>
                       <h4 className="text-white font-bold text-xs uppercase mb-1">Architecture</h4>
                       <p className="text-[10px] text-slate-500 leading-relaxed italic">Scaling React & NestJS environments for neural data flows.</p>
                    </div>
                  </div>
                </div>
              )}

              {activeTab === 'engine' && (
                <div className="p-10 space-y-8 animate-in fade-in slide-in-from-right-6 duration-700">
                  <div>
                    <h3 className="text-white font-black text-[11px] uppercase tracking-[0.3em] mb-6">Technical_Inventory</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                       <section className="space-y-4">
                          <h4 className="text-[9px] font-black text-cyan-500/60 uppercase tracking-widest">Core_Processing</h4>
                          <div className="flex flex-wrap gap-2">
                             {inventory.languages.concat(inventory.frameworks).map(item => (
                               <span key={item} className="px-3 py-1.5 bg-white/5 border border-white/5 rounded-xl text-[10px] font-bold text-slate-300 hover:text-cyan-400 transition-colors cursor-default">{item}</span>
                             ))}
                          </div>
                       </section>
                       <section className="space-y-4">
                          <h4 className="text-[9px] font-black text-purple-500/60 uppercase tracking-widest">Neural_Modules</h4>
                          <div className="flex flex-wrap gap-2">
                             {inventory.ai_ml.map(item => (
                               <span key={item} className="px-3 py-1.5 bg-purple-500/5 border border-purple-500/10 rounded-xl text-[10px] font-bold text-purple-300 hover:text-white transition-colors cursor-default">{item}</span>
                             ))}
                          </div>
                       </section>
                    </div>
                  </div>

                  <div className="pt-8 border-t border-white/5">
                    <h3 className="text-white font-black text-[11px] uppercase tracking-[0.3em] mb-6">Mission_Status</h3>
                    <div className="space-y-3">
                       {quests.map((q, i) => (
                         <div key={i} className="flex items-center justify-between p-4 bg-white/[0.02] border border-white/5 rounded-2xl hover:bg-white/[0.05] transition-all">
                            <div className="flex items-center gap-4">
                               <div className="w-10 h-10 bg-black rounded-xl flex items-center justify-center text-cyan-500 border border-white/10">
                                  {q.status.includes('STABLE') ? <Shield size={18}/> : <Activity size={18} className="animate-pulse"/>}
                               </div>
                               <div>
                                  <div className="text-xs font-bold text-white uppercase">{q.title}</div>
                                  <div className="text-[9px] text-slate-500 uppercase">{q.org}</div>
                               </div>
                            </div>
                            <span className={`text-[9px] font-mono font-bold ${q.color}`}>{q.status}</span>
                         </div>
                       ))}
                    </div>
                  </div>
                </div>
              )}

              {activeTab === 'neural' && (
                <div className="flex-1 flex flex-col h-full animate-in zoom-in-95 duration-500">
                  <div className="p-6 border-b border-white/5 bg-white/5 flex items-center justify-between">
                     <div className="flex items-center gap-3">
                        <div className="w-2 h-2 rounded-full bg-cyan-500 animate-pulse"></div>
                        <span className="text-[10px] font-black text-white uppercase tracking-[0.3em]">Gemini_Neural_Uplink</span>
                     </div>
                     <span className="text-[8px] font-mono text-slate-500">REALTIME_AI_PROCESSING</span>
                  </div>

                  <div className="flex-1 overflow-y-auto p-8 space-y-6 scrollbar-hide">
                    {chatHistory.map((chat, i) => (
                      <div key={i} className={`flex ${chat.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`max-w-[80%] p-5 rounded-[2rem] text-xs ${
                          chat.role === 'user' 
                            ? 'bg-cyan-500 text-black font-bold rounded-tr-none shadow-xl' 
                            : 'bg-white/5 border border-white/10 text-slate-300 rounded-tl-none font-mono leading-relaxed'
                        }`}>
                          {chat.text}
                        </div>
                      </div>
                    ))}
                    {isTyping && (
                      <div className="flex justify-start">
                         <div className="bg-white/5 p-4 rounded-full border border-white/10 flex items-center gap-2">
                            <div className="w-1.5 h-1.5 bg-cyan-500 rounded-full animate-bounce"></div>
                            <div className="w-1.5 h-1.5 bg-cyan-500 rounded-full animate-bounce delay-75"></div>
                            <div className="w-1.5 h-1.5 bg-cyan-500 rounded-full animate-bounce delay-150"></div>
                         </div>
                      </div>
                    )}
                  </div>

                  <form onSubmit={handleChat} className="p-8 border-t border-white/5 bg-black/40">
                    <div className="relative group">
                      <input 
                        type="text" 
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="Inquire the Core AI..."
                        className="w-full bg-white/5 border border-white/10 rounded-2xl py-4 px-6 pr-14 text-xs text-white focus:outline-none focus:border-cyan-500/50 transition-all placeholder:text-slate-600"
                      />
                      <button type="submit" className="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 bg-cyan-500 text-black rounded-xl flex items-center justify-center hover:scale-110 active:scale-95 transition-transform shadow-lg">
                        <Send size={18} />
                      </button>
                    </div>
                  </form>
                </div>
              )}

            </div>
          </main>
        </div>

        <footer className="mt-12 py-8 border-t border-white/5 flex flex-wrap justify-between items-center gap-6 text-[9px] font-mono text-slate-600 tracking-[0.4em] uppercase">
          <p>© 2027_AMIT_KUMAR_OS // ALL SYSTEMS NOMINAL</p>
          <div className="flex items-center gap-6">
             <span className="flex items-center gap-2 text-cyan-500/50"><Shield size={12}/> ENCRYPTION: SHA-1024</span>
             <span className="flex items-center gap-2"><Binary size={12}/> CORE_VERSION_2.0.7</span>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default App;
