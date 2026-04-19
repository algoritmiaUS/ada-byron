import java.io.*;
import java.util.*;

public class pablo {

    static int[] buildPi(String p) {
        int m = p.length();
        int[] pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) j++;
            pi[i] = j;
        }
        return pi;
    }

    static List<Integer> kmpOccurrences(String s, String p) {
        List<Integer> occ = new ArrayList<>();
        int[] pi = buildPi(p);

        int n = s.length();
        int m = p.length();
        int j = 0;

        for (int i = 0; i < n; i++) {
            while (j > 0 && s.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (s.charAt(i) == p.charAt(j)) j++;
            if (j == m) {
                occ.add(i - m + 1);
                j = pi[j - 1];
            }
        }
        return occ;
    }

    static class Event {
        int id, start;
        Event(int id, int start) {
            this.id = id;
            this.start = start;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String dna = br.readLine();
        String line = br.readLine();
        int k = Integer.parseInt(br.readLine().trim());

        if (dna == null || line == null) {
            System.out.println(0);
            return;
        }

        // Parsear motivos y eliminar duplicados conservando orden
        String[] parts = line.trim().isEmpty() ? new String[0] : line.trim().split("\\s+");
        LinkedHashSet<String> set = new LinkedHashSet<>();
        for (String x : parts) set.add(x);
        List<String> patterns = new ArrayList<>(set);

        int n = dna.length();
        int m = patterns.size();

        if (k > m) {
            System.out.println(0);
            return;
        }

        @SuppressWarnings("unchecked")
        ArrayList<Event>[] events = new ArrayList[n];
        for (int i = 0; i < n; i++) events[i] = new ArrayList<>();

        for (int id = 0; id < m; id++) {
            String p = patterns.get(id);
            List<Integer> occ = kmpOccurrences(dna, p);
            int len = p.length();

            for (int start : occ) {
                int end = start + len - 1;
                events[end].add(new Event(id, start));
            }
        }

        int[] latestStart = new int[m];
        Arrays.fill(latestStart, -1);

        int answer = Integer.MAX_VALUE;

        for (int r = 0; r < n; r++) {
            for (Event ev : events[r]) {
                latestStart[ev.id] = Math.max(latestStart[ev.id], ev.start);
            }

            ArrayList<Integer> active = new ArrayList<>();
            for (int x : latestStart) {
                if (x != -1) active.add(x);
            }

            if (active.size() >= k) {
                active.sort(Collections.reverseOrder());
                int L = active.get(k - 1);
                answer = Math.min(answer, r - L + 1);
            }
        }

        System.out.println(answer == Integer.MAX_VALUE ? 0 : answer);
    }
}